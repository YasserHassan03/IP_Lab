fs = 1000;      % Sampling rate in Hz
fc = 20;        % Cutoff frequency in Hz
rp = 0.5;       % Passband ripple in dB
rs = 65;        % Stopband attenuation in dB

% Design the filter
lpFilt = designfilt('lowpassfir', 'PassbandFrequency', fc, ...
                    'StopbandFrequency', 1.2*fc, 'PassbandRipple', rp, ...
                    'StopbandAttenuation', rs, 'SampleRate', fs);

% View the filter coefficients
lpFilt.Coefficients

% Visualize the filter response
fvtool(lpFilt);
