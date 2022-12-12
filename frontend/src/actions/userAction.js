import axios from 'axios'
import {
    USER_GET_REQUEST,
    USER_GET_SUCESS,
    USER_GET_FAIL,

    USER_ADD_REQUEST, 
    USER_ADD_SUCESS , 
    USER_ADD_FAIL,

    USER_UPDATE_REQUEST, 
    USER_UPDATE_SUCESS , 
    USER_UPDATE_FAIL,

   USER_RECOMENDATIONS_REQUEST,
    USER_RECOMENDATIONS_SUCESS,
    USER_RECOMENDATIONS_FAIL,
} from '../constants/userConstans'


export const registerUser = (name, uid, age,sex, genres) => async (dispatch) => {
    try {
        
        dispatch({type: USER_ADD_REQUEST})

        const { data } = await axios.post(
            '/api/users/register/',
            { 'name': name, 'uid': uid, 'age': age, 'sex':sex, 'genres':genres}
        )

        dispatch({
            type: USER_ADD_SUCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: USER_ADD_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}

export const updateUser = (name, uid, age, sex) => async (dispatch) => {
  
    try {
       
        dispatch({type: USER_UPDATE_REQUEST})

        const { data } = await axios.put(
            `/api/users/update/${uid}`,
            { 'name': name, 'uid': uid, 'age': age, 'sex':sex}
        )

        dispatch({
            type: USER_UPDATE_SUCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: USER_UPDATE_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const getUser = (uid) => async (dispatch) => {
    try{
        dispatch({type: USER_GET_REQUEST})
        const {data} =  await axios.get(`/api/users/data/${uid}`)
        dispatch({
            type: USER_GET_SUCESS,
            payload:data
        })

    }catch(error){
        dispatch({
            type: USER_GET_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}

export const getUserRecomendation = (uid) => async (dispatch) => {
    try{
        dispatch({type: USER_RECOMENDATIONS_REQUEST})
        const {data} =  await axios.get(`/api/user/algo/${uid}`)
        dispatch({
            type: USER_RECOMENDATIONS_SUCESS,
            payload: data
        })

    }catch(error){
        dispatch({
            type: USER_RECOMENDATIONS_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}