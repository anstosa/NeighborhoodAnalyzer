% generate data for clustering
% we will generate 3 clusters
% cluster 1: number of samples n1
  n1 = 42;
% taxpayer age -- normal distribution with mean 30 and variance 5
  tx = normrnd(30,5,1,n1);
% walkability -- normal distribution with mean 90 and variance of 5
  w = normrnd(90,5,1,n1);
% distance to park -- normal distribution with mean of 2 and variance of
% 0.3
  dp = normrnd(2,0.3,1,n1);
% square footage -- normal distribution with mean of 1400 and variance of
% 100
  sqf = normrnd(1400,100,1,n1);
% lot size -- normal distribution with mean of 0.25 and variance of 0.05
  lot = normrnd(0.25,0.05,1,n1);
% bedrooms -- integer random {2,3,4} average around 3 with ratio 20% are
% 2's
  a = inv([ 3 4 ; 1 1])*[3*n1 - 0.2*2*n1; n1 - 0.2*n1];
  a1 = floor(0.2*n1); a2 = floor(a(1)); a3 = n1 - a1 - a2;
  temp = [2*ones(1,a1) 3*ones(1,a2) 4*ones(1,a3)];
  br = temp(randperm(n1));
% bathrooms -- integer random {1,2} average around 1.8
  a2 = floor(0.8*n1); a1 = n1 - a2;
  temp = [1*ones(1,a1) 2*ones(1,a2)];
  bh = temp(randperm(n1));
% garage -- integer random {1,2} average around 1.7
  a2 = floor(0.7*n1); a1 = n1 - a2;
  temp = [1*ones(1,a1) 2*ones(1,a2)];
  g = temp(randperm(n1));
% off street parking -- integer random {1,2} average around 1.6
  a2 = floor(0.6*n1); a1 = n1 - a2;
  temp = [1*ones(1,a1) 2*ones(1,a2)];
  os = temp(randperm(n1));
% distance to public schools -- integer {0,1} average around 0.8
  a2 = floor(0.8*n1); a1 = n1 - a2;
  temp = [zeros(1,a1) 1*ones(1,a2)];
  pubsc = temp(randperm(n1));
% distance to private schools -- integer {0,1} average around 0.2
  a2 = floor(0.2*n1); a1 = n1 - a2;
  temp = [zeros(1,a1) 1*ones(1,a2)];
  prvsc = temp(randperm(n1));
% access to highway -- integer {0,1} average 0.7
  a2 = floor(0.7*n1); a1 = n1 - a2;
  temp = [zeros(1,a1) 1*ones(1,a2)];
  hway = temp(randperm(n1));
% export as xls file
  A = {'tax age'; 'walk sc'; 'dist to park'; 'sq ft'; 'lot sz'; 'bedroom'; ...
       'bathroom'; 'garage'; 'off street'; 'pub school'; 'prv school'; 'hway acces'};
  B = [ tx; w; dp; sqf; lot; br; bh; g; os; pubsc; prvsc; hway];

  xlswrite('junk.xls',A);
  xlswrite('junk.xls',B,1,'B1');
