#include<stdio.h>
#include<stdlib.h>

char* entrada = "aabc";
int tk_pos = 0;

void casar_token(char tk) {
	if(tk == entrada[tk_pos]) {
		tk_pos++;
	}else{
		printf("Era esperado %c mas encontrado %c\n",tk,entrada[tk_pos]);
		exit(0);
	}
}

void naoterminal_X() {
	if(entrada[tk_pos] == 'b') {
		printf("produzir X->bX\n");
		casar_token('b');
		naoterminal_X();
	}else{
		printf("produzir X->a\n");
		casar_token('a');
	}
}

void naoterminal_S() {
	
	if(entrada[tk_pos] == 'a') {
		printf("produzir S->aXb\n");
		casar_token('a');
		naoterminal_X();
		casar_token('b');
	}else if(entrada[tk_pos] == 'b') {
		printf("produzir S->bXa\n");
		casar_token('b');
		naoterminal_X();
		casar_token('a');
	}else{
		printf("produzir S->c\n");
		casar_token('c');
	}
}

int main() {
	naoterminal_S();
	return 0;
}
