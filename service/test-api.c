#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

int getStatus(){
	CURL *curl;
	CURLcode response;

	curl_global_init(CURL_GLOBAL_ALL);

	curl = curl_easy_init();
	if(curl){
		curl_easy_setopt(curl,CURLOPT_URL,"http://localhost:8000/status");
		response = curl_easy_perform(curl);

		if(response != CURLE_OK){
			fprintf(stderr,"Request failed: %s\n",curl_easy_strerror(response));			
		}
		else{
			char *str = curl_easy_strerror(response);
			printf("\n");
			while(*str){
				printf("%c",*str);
				str++;
			}
			if(str[0] == 't')
				return 1;
			else
				return 0;
		}
		curl_easy_cleanup(curl);
	}
	curl_global_cleanup();
}

int main(){
	//printf("%s\n",getStatus());
	//char *x = curl_easy_strerror(getStatus());
	//printf("%s\n",x);
	int x = getStatus();
	printf("Status: %d\n",x);
}
