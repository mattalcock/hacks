from difflib import SequenceMatcher

""" Returns a value between 0 and 1 of 2 string sequences """
def compare_str(a,b):
	s = SequenceMatcher(lambda x: x == " ", a.lower(), b.lower())
	return s.ratio()

def simular_str(a,b, threshold=0.7):
	return compare_str(a,b)>threshold


if __name__ == '__main__':


	#Same Garments
	a = "Black Skirt - 16"
	b = "black Skirt - 16"

	print compare_str(a,b)	#1.0
	print simular_str(a,b)	#True

	#Same Garments
	a = "Black Skirt - 16"
	b = "black skirt 16"

	print compare_str(a,b)	#0.769
	print simular_str(a,b)	#True

	#Same Garments
	a = "Black Skirt - 16"	
	b = "black - 16"		

	print compare_str(a,b)	#0.769230769231
	print simular_str(a,b)	#True

	#Different Garments
	a = "Black Skirt - 16"	
	b = "Black Skirt - 14"	

	print compare_str(a,b)	#0.9375
	print simular_str(a,b)	#True  - Wrong


