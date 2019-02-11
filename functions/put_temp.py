from firebase import firebase

temp = 87879

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
firebase.put('mines','temp',temp)
#print (put)
