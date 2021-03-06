clc;
clear;
%读取图像
filepathsrc = 'database\';
fileform{1} = 'database\RS_*.bmp';
fileform{2} = 'database\Pa_*.bmp';
fileform{3} = 'database\Cr_*.bmp';
fileform{4} = 'database\PS_*.bmp';
fileform{5} = 'database\In_*.bmp';
fileform{6} = 'database\Sc_*.bmp';
ALL_IMG=zeros(200,200,300,6);
for ii=1:6
	file = dir(fileform{ii});
%创建缺陷矩阵
	IMG=zeros(200,200,300);
	for i = 1:300
		img=imread([file(i).name]);
		IMG(:,:,i)=img;
	end
	ALL_IMG(:,:,:,ii)=IMG;
end
%按缺陷类别存储
RS_img=reshape(ALL_IMG(:,:,:,1),200,200,300);
Pa_img=reshape(ALL_IMG(:,:,:,2),200,200,300);
Cr_img=reshape(ALL_IMG(:,:,:,3),200,200,300);
PS_img=reshape(ALL_IMG(:,:,:,4),200,200,300);
In_img=reshape(ALL_IMG(:,:,:,5),200,200,300);
Sc_img=reshape(ALL_IMG(:,:,:,6),200,200,300);
%保存读取的数据
save('imgdata.mat','RS_img','Pa_img','Cr_img','PS_img','In_img','Sc_img');
I =Pa_img(:,:,1)
imshow(I/256); %像素值映射到0~1
