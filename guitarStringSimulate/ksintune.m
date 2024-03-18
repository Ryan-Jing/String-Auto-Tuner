function Y=ksintune(f,length)
    %Karplus-Strong model with Lagrange interpolation filter to account
    %for fractional delay
    %   ks(f,length)
    %   f=frequency
    %   length=time (seconds)
    fs=44100;
    N=fix(fs/f);
    X=zeros(1,length*fs);

    l = lagrange(3,f/fs);

    %loop filter
    h = [.5 .5];

    %           L(z)z^-N
    b1=[zeros(1,N) l];

    %       1 - H(z)L(z)z^-N
    a1=[1 zeros(1,N-1) -conv(l, h)];



    Zi = rand(1, max( max(size(a1)), max(size(b1))) -1);

    Y=filter(b1,a1,X,Zi);
