or(int x=0;x<r;x++){
        for(int y=0;*(p+x*c+y)!='\0';y++){
            *(p+x*c+y)+=32;
        }   
    }