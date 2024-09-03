
edge_mean = dlmread('edge_entropy_N200_mean.txt');
edge_std = dlmread('edge_entropy_N200_std.txt');

deg_mean = dlmread('degree_entropy_N200_mean.txt');
deg_std = dlmread('degree_entropy_N200_std.txt');

figure(1); clf; hold on
d1 = edge_mean-edge_std;
d2 = edge_mean+edge_std;
fill([0:100 100:-1:0],[d1; d2(101:-1:1)],'r','edgecolor','none','FaceAlpha',0.5)
plot(0:100,edge_mean,'r-','linewidth',2)

xlabel('Lloyds Iteration')
ylabel('Edge Entropy')

box on
% set(gca,'XScale','log') % doesn't like points a x=0
set(gca,'fontsize',20)


figure(2); clf; hold on
d3 = deg_mean-deg_std;
d4 = deg_mean+deg_std;
fill([0:100 100:-1:0],[d3; d4(101:-1:1)],'b','edgecolor','none','FaceAlpha',0.5)
plot(0:100,deg_mean,'b-','linewidth',2)

xlabel('Lloyds Iteration')
ylabel('Degree Entropy')

box on
% set(gca,'XScale','log') % doesn't like points a x=0
set(gca,'fontsize',20)