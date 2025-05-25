% The function to handle inf, NaN and extremely small values
function [I, extreme_mask] = handleinvalidValues(I)
    % Create the mask matrix of invalid values
    nan_mask = isnan(I);  % position of NaN
    inf_mask = isinf(I);  % position of Inf and -Inf
    small_value_mask = I < -3.4028e+37;  % position of extremely small values
    extreme_mask  = nan_mask | inf_mask | small_value_mask;  % mask matrix
    
    if any(extreme_mask(:))
        % Fill in the invalid values with the mean of valid values.
        valid_mask = ~extreme_mask;
        valid_mean = mean(I(valid_mask), 'omitnan');
        I(extreme_mask) = valid_mean; 
    end
end