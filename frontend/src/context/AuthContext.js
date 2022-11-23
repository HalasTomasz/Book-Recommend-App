import React, {createContext, useState, useEffect, useContext} from 'react'
import { auth } from '../firebase';
import {createUserWithEmailAndPassword, sendPasswordResetEmail, signInWithEmailAndPassword, signOut, updateEmail, updatePassword } from "firebase/auth";
import { registerUser } from "../actions/userAction";
import {useDispatch } from 'react-redux'
const AuthContext = createContext()

export function useAuth(){
    return useContext(AuthContext)
}

export function AuthProvider({children}) {

    const [currentUser, setCurrentUser] = useState()
    const [loading,setLoading] = useState(true)
    const dispatch = useDispatch()

    async function signup(email,password, name, age, sex, genres){
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        dispatch(registerUser(name, user.uid, age, sex, genres)); // HERE WE CAN ADD GENRE
    }

    function login(email, password){
        return signInWithEmailAndPassword(auth, email, password)
    }

    function logout(){
        return signOut(auth)
    }

    function resetpassword(email){
        return sendPasswordResetEmail(auth,email)
    }

    function updateemail(email){
        return updateEmail(currentUser,email)
    }

    function updatepassword(password){
        return updatePassword(currentUser, password)
    }

    useEffect(() =>{
     
        const unsub = auth.onAuthStateChanged(user=>{
            setCurrentUser(user)
            setLoading(false)
        })
        return unsub

    },[])



    const value = {
        currentUser,
        signup,
        login,
        logout,
        resetpassword,
        updateemail,
        updatepassword
    }
    
    return(
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>    
    )
}