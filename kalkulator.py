def dodawanie(a, b):
	return a + b

try:
	l1 = int(input())
	l2 = int(input())
	dodawanie(dodawania(l1, l2))
except:
	print("Program zakonczył się nieoczekiwanym błędem")
	print("Możesz go zgłosić pod adresem pomoc@autor.pl")