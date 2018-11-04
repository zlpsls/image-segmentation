function	[psnr]	= PSNR( img,img_en,inde)
%UNTITLED3 此处显示有关此函数的摘要
% 此处显示详细说明
psnr=zeros(1,size(inde,2)); 
for i=1:size(inde,2)
    imgs=img(:,:,inde(i));
    %disp(imgs;
    img_ens=img_en(:,:,inde(i)); 
    %img_ens;
    mse=sum(sum((uint8(imgs)-uint8(img_ens)).*(uint8(imgs)-uint8(img_ens))))/(200*200);
    psnr(i)=10*log10(255^2/mse);
end 
end
