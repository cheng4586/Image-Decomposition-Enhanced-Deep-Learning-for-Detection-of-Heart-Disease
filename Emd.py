import matplotlib.pyplot as plt
import numpy as np
import emd

class Solution:
    def emd_sift(self):
        sample_rate = 1000
        seconds = 10
        num_samples = sample_rate*seconds

        time_vect = np.linspace(0, seconds, num_samples)

        freq = 5

        # Change extent of deformation from sinusoidal shape [-1 to 1]
        nonlinearity_deg = 0.25

        # Change left-right skew of deformation [-pi to pi]
        nonlinearity_phi = -np.pi/4

        # Compute the signal

        # Create a non-linear oscillation
        x = emd.simulate.abreu2010(freq, nonlinearity_deg, nonlinearity_phi, sample_rate, seconds)

        x += np.cos(2 * np.pi * 1 * time_vect)        # Add a simple 1Hz sinusoid
        x -= np.sin(2 * np.pi * 2.2e-1 * time_vect)   # Add part of a very slow cycle as a trend

        def create_noise(X, N, snr):
            noise = np.random.randn(N)
            snr = 10 ** (snr/10)
            power = np.mean(np.square(X))
            npower = power/snr
            noise = noise * np.sqrt(npower)
            return noise

        noise_1 = create_noise(x, 5000, 35)
        noise_2 = create_noise(x, 5000, 20)
        print(type(noise_1))
        noise = np.append(noise_1, noise_2)
        x_noise = x + noise
        # Visualise the time-series for analysis
        plt.figure(figsize=(12, 4))


        # Get the default configuration for a sift
        config = emd.sift.get_config('sift')
        # Extract envelope options
        env_opts = config['envelope_opts']

        # Compute upper and lower envelopes
        upper_env = emd.sift.interp_envelope(x_noise, mode='upper', **env_opts)
        lower_env = emd.sift.interp_envelope(x_noise, mode='lower', **env_opts)

        # Compute average envelope
        avg_env = (upper_env+lower_env) / 2
        sift_1 = x_noise - avg_env

        # Compute upper and lower envelopes
        upper_env = emd.sift.interp_envelope(sift_1, mode='upper', **env_opts)
        lower_env = emd.sift.interp_envelope(sift_1, mode='lower', **env_opts)

        # Compute average envelope
        avg_env = (upper_env + lower_env) / 2
        sift_2 = sift_1 - avg_env
        return x, x_noise, sift_1, sift_2
        # plt.plot(x)
        # plt.show()

if __name__ == '__main__':

    x, x_noise, sift_1, sift_2 = first_unique = Solution().emd_sift()
    plt.figure(1)
    ax1 = plt.subplot(411)
    ax1 = plt.plot(x)
    ax1 = plt.subplot(412)
    ax1 = plt.plot(x_noise)
    ax1 = plt.subplot(413)
    ax1 = plt.plot(sift_1)
    ax1 = plt.subplot(414)
    ax1 = plt.plot(sift_2)
    plt.show()

