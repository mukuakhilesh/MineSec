from firebase import firebase

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
temp_=firebase.get('mines','temp')
#print(temp)