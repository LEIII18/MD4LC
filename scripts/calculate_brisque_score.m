clc;clear all;
rasterpath = 'data\54_74E5_56N.tif';%write your target raster here
I = imread(rasterpath);

%% remove the first row and column
% some raster's first column and row is invalid value
if min(size(I))>2
    I=I(2:end-1,2:end-1);
end

%% handle inf, NaN and extremely small values in images, preserve inf and NaN, and mark them
[I, nan_inf_mask] = handleinvalidValues(I);  % Call the function to handle inf, NaN and extremely small values in remote sensing data
if all(~nan_inf_mask(:))  % if no inf, NaN and extremely small values
    img_quality = brisque(I); 
elseif all(nan_inf_mask(:)) % if pixels are all inf, NaN and extremely small values
    img_quality = NaN; 
else % Not all are inf, NaN, and extremely small values.
    % Calculate the proportion of invalid-value pixels and provide a discounted quality assessment value
    img_quality = brisque(I) * (1 - sum(nan_inf_mask(:)) / numel(I));
end