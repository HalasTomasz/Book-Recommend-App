import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBnWmv0Mk433qTCPu-hoMxVcXZfgf8UUtQ",
    authDomain: "book-tools-db.firebaseapp.com",
    projectId: "book-tools-db",
    storageBucket: "book-tools-db.appspot.com",
    messagingSenderId: "41052229263",
    appId: "1:41052229263:web:70b33d31706103c42beafa",
    measurementId: "G-23LBSMDLGH"
  };

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app 