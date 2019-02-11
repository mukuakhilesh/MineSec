from firebase import firebase

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
ch4_=firebase.get('mines','ch4')
#print(ch4_)