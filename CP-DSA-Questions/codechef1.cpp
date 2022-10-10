Question:-
https://www.codechef.com/submit/FILL01

Solution:-
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin>>t;
	while(t--){
	    int n,k,count=0; cin>>n>>k;
	    string s; cin>>s;
	    for(int i=0;i<n;){
	        int c=0;
	        if(s[i]=='0'){
	            c++; i++;
	            while(s[i]=='0'){
	                c++; i++;
	            }
	            if(c>=k){
	                count=count+(c/k);
	            }
	        }
	        else{
	            i++;
	        }
	    }
	    cout<<count<<"\n";
	}
	return 0;
}
