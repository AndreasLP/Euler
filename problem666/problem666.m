K = 500;
M = 10;


r = zeros((K+1)*M,1);
r(1) = 306;
for i = 2:((K+1)*M)
    r(i) = mod(r(i-1)^2,10007);
end
q = mod(r,5);

% each column is a child vector
%children = zeros(K,2,K);
children = zeros(K,5,K);
%p = zeros(K,2);
p = zeros(K,5);
for i = 0:(K-1)
    j = i+1;
    vals = q(((i*M):(i*M+M-1)) + 1);
    len = length(vals);
    p(j,:) = [sum(vals==0) sum(vals==1) ...
        sum(vals==2) sum(vals==3) sum(vals==4)]/len;
    
    children(j,2,j) = 2;
    children(mod(2*i,K)+1,3,j) = 1;
    children(mod(i*i+1,K)+1,4,j) = 3;
    
    children(mod(j,K)+1,5,j) = 1;
    children(j,5,j) = 1;
    
end

s = zeros(K,1);
s(1) = 0.5;

%disp([f(1,s,p,children);f(2,s,p,children)]);
for i=1:30
s = sum(p.*permute(prod(s.^children),[3 2 1]),2);%[f(1,s,p,children);f(2,s,p,children)];
    if mod(i,10)==0
        fprintf("%.8f\n",s(1));
    end
end




