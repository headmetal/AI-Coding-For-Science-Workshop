% detrend_season.m - remove linear trend and mean seasonal cycle from a monthly series
% input: monthly_series.csv with columns year, month, value (header row)
M = csvread('monthly_series.csv', 1, 0);
v = M(:,3);
n = length(v);
% use only the first 20 years for the climatology
clim = zeros(12,1);
for m = 1:12
    idx = m:12:(20*12);
    clim(m) = mean(v(idx));
end
anom = v - repmat(clim, n/12, 1);
% detrend (removes mean and linear trend)
anom_dt = detrend(anom);
fprintf('mean anomaly: %.4f\n', mean(anom));
fprintf('std detrended: %.4f\n', std(anom_dt));
fprintf('max detrended at index: %d\n', find(anom_dt == max(anom_dt)));
fprintf('clim Jan Jul: %.3f %.3f\n', clim(1), clim(7));
