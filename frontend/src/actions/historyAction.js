import axios from "axios"
import {BOOK_HISTORY_ADD_REQUEST, 
        BOOK_HISTORY_ADD_SUCESS,
        BOOK_HISTORY_ADD_FAIL,
    
        BOOK_HISTORY_GET_REQUEST,
        BOOK_HISTORY_GET_SUCESS,
        BOOK_HISTORY_GET_FAIL,

        BOOK_HISTORY_RETURN_REQUEST,
        BOOK_HISTORY_RETURN_SUCESS,
        BOOK_HISTORY_RETURN_FAIL,
    } 

from '../constants/historyConstans'


export const getListHistory = (uid) => async (dispatch) => {
    try{
        dispatch({type: BOOK_HISTORY_GET_REQUEST})
        const {data} =  await axios.get(`/api/user/history/${uid}`)
        dispatch({
            type: BOOK_HISTORY_GET_SUCESS,
            payload:data
        })

    }catch(error){
        dispatch({
            type: BOOK_HISTORY_GET_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}

export const addToHistory = (uid, book_id) => async (dispatch, getState) =>{
    try{
        dispatch({type: BOOK_HISTORY_ADD_REQUEST})
        const{data} = await axios.post('/api/user/set/history/', {'uid':uid,'book_id':book_id})

        dispatch({
            type: BOOK_HISTORY_ADD_SUCESS,
            payload: data
            })
    }catch (error) {
        dispatch({
            type: BOOK_HISTORY_ADD_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }

    //localStorage.setItem('historyBook', JSON.stringify(getState().historyList.historyBook))
}

export const returnHistoryBook = (id, rent_id) => async (dispatch) => {
    try{
        dispatch({type: BOOK_HISTORY_RETURN_REQUEST})
        const {data} =  await axios.put('/api/user/history/return/', {'book_id':id,'rent_id':rent_id})
        dispatch({
            type: BOOK_HISTORY_RETURN_SUCESS,
            payload:data
        })

    }catch(error){
        dispatch({
            type: BOOK_HISTORY_RETURN_FAIL,
            payload: error.responose && error.responose.data.message 
            ? error.responose.data.message
            : error.message,
             
        }) 

    }
}
