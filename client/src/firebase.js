import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, signInWithPhoneNumber } from "firebase/auth";
import { useDispatch } from "react-redux";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAPNBacR_8gqemQgjNeluYZVsXcow2onZU",
  authDomain: "presspesa-tanzania.firebaseapp.com",
  projectId: "presspesa-tanzania",
  storageBucket: "presspesa-tanzania.appspot.com",
  messagingSenderId: "12949444092",
  appId: "1:12949444092:web:c2b5717fc6f04598294e79",
  measurementId: "G-E3WZPJYN20",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const analytics = getAnalytics(app);
const db = getFirestore(app)

export { app, auth, analytics, db };
