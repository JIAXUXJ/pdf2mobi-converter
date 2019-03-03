void capitalize(char *s)
{
    char *p;
    for (p = s; *p; p++) {
        if(p!='\0'){
            *p = toupper(*p);
        }  
    }


}
int main(){
	printf("hello\n");
}