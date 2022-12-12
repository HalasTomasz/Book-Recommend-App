import axios from 'axios'
import {
    BOOK_LIST_REQUEST, 
    BOOK_LIST_SUCESS, 
    BOOK_LIST_FAIL,
    
    BOOK_DATA_REQUEST, 
    BOOK_DATA_SUCESS, 
    BOOK_DATA_FAIL,
} from '../constants/bookConstans'

export const listBooks = () => async (dispatch) => {
    try{
        dispatch({type: BOOK_LIST_REQUEST})
        const {data} =  await axios.get('/api/books/')
        dispatch({
            type: BOOK_LIST_SUCESS,
            payload:data
        })

    }catch(error){
        dispatch({
            type: BOOK_LIST_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}

export const listBookData = (id, uid) => async (dispatch) => {
    try{
        dispatch({type: BOOK_DATA_REQUEST})
        const {data} =  await axios.get(`/api/books/${id}`,  {
            params: {
                user: uid
            }
        })
        dispatch({
            type: BOOK_DATA_SUCESS,
            payload: data
        })

    }catch(error){
        dispatch({
            type: BOOK_DATA_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}