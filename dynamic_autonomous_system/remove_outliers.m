clear all
close all

file=fopen('matlab_data.txt','r');

if(file == -1)
    error('Could not open file')
end

data=textscan(file, '%f');
y=data{1};

x=(1:size(y));
%x=x';

%
%boxplot(y)
[B, stats]=robustfit(x,y)

scatter(x, y, 'r')
hold on
plot(x, B(1)+B(2)*x)
plot(x, y+stats.resid, 'g')

