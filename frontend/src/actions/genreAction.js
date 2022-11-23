import axios from 'axios'
import {
    GENRE_USER_REQUEST,
    GENRE_USER_SUCESS,
    GENRE_USER_FAIL,
    
    GENRE_LIST_REQUEST, 
    GENRE_LIST_SUCESS, 
    GENRE_LIST_FAIL,

    GENRE_UPDATE_REQUEST, 
    GENRE_UPDATE_SUCESS, 
    GENRE_UPDATE_FAIL,
} from '../constants/genreConstans'

export const listGenre= () => async (dispatch) => {
    try{
        dispatch({type: GENRE_LIST_REQUEST})
        const {data} =  await axios.get('/api/books/genre')

        dispatch({
            type: GENRE_LIST_SUCESS,
            payload:data
        })

    }catch(error){
        dispatch({
            type: GENRE_LIST_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}

export const listUserGenre= (auth_id) => async (dispatch) => {
    try{
        dispatch({type: GENRE_USER_REQUEST})
        const {data} =  await axios.get(`/api/user/genre/${auth_id}`)

        dispatch({
            type: GENRE_USER_SUCESS,
            payload: data
        })

    }catch(error){
        dispatch({
            type: GENRE_USER_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}

export const updateUserGenre= (genre_data, auth_id) => async (dispatch) => {
    try{
        dispatch({type: GENRE_UPDATE_REQUEST})
        const {data} =  await axios.post('/api/user/update/genre/',  {'new_genres': genre_data, 'uid': auth_id})

        dispatch({
            type: GENRE_UPDATE_SUCESS,
            payload: data
        })

    }catch(error){
        dispatch({
            type: GENRE_UPDATE_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}