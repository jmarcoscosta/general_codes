func = @(t) 4*cos(2*pi*100000*t)+3*cos(2*pi*5000*t);
% PERÍODO DA FUNÇÃO
T = 1/5000;
% N MÁXIMO
maxN = 21;

an = @(t,n) func(t).*cos(n*pi*t/(T/2))./(T/2);
bn = @(t,n) func(t).*sin(n*pi*t/(T/2))./(T/2);

ran = [];
rbn = [];

% CÁLCULO DO AN
for a = 0:maxN
    i = integral(@(x) an(x,a),-T/2,T/2);
    if i < 1e-05
        i = 0;
    end
    echo = ['Para n = ', num2str(a), ': an = ', num2str(i)];
    disp(echo)
    %ran(a+1) = i;
    ran = [ran i];
end

disp(' ');

% CÁLCULO DO BN
for b = 0:maxN
    i = integral(@(x) bn(x,b),-T/2,T/2);
    if i < 1e-05
        i = 0;
    end
    echo = ['Para n = ', num2str(b), ': bn = ', num2str(i)];
    disp(echo)
    %rbn(a+1) = i;
    rbn = [rbn i];
end

% SÉRIE DE FOURIER
t = linspace(-2*T,2*T,10000);
y = ran(1)/2;
for i = 2:maxN+1
    y = y + ran(i)*cos((i-1)*pi*t/(T/2));
    y = y + rbn(i)*sin((i-1)*pi*t/(T/2));
end

figure;
subplot(211);
plot(t,y,'b');
subplot(212);
plot(t,func(t),'r');
