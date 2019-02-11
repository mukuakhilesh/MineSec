from firebase import firebase

ch4 = 87879

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
firebase.put('mines','ch4',ch4)
#print (put)





