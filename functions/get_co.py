from firebase import firebase

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
co_=firebase.get('mines','co')
#print(co_)