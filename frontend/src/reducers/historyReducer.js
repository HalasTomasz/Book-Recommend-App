import {
    BOOK_HISTORY_ADD_REQUEST,
    BOOK_HISTORY_ADD_SUCESS,
    BOOK_HISTORY_ADD_FAIL,

    BOOK_HISTORY_GET_REQUEST,
    BOOK_HISTORY_GET_SUCESS,
    BOOK_HISTORY_GET_FAIL,

    BOOK_HISTORY_RETURN_REQUEST,
    BOOK_HISTORY_RETURN_SUCESS,
    BOOK_HISTORY_RETURN_FAIL,

} from '../constants/historyConstans'

export const getListHistoryReducer= (state = {user_history: []}, action) =>{
    switch(action.type){
        case BOOK_HISTORY_GET_REQUEST:
            return {loading: true, user_history: []}

        case BOOK_HISTORY_GET_SUCESS:
            return {loading: false, user_history: action.payload}
        
        case BOOK_HISTORY_GET_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}

export const setListHistoryReducer= (state = {}, action) =>{
    switch(action.type){
        case BOOK_HISTORY_ADD_REQUEST:
            return {loading: true }

        case BOOK_HISTORY_ADD_SUCESS:
            return {loading: false, new_user_history: action.payload}
        
        case BOOK_HISTORY_ADD_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}

export const updateListHistoryReducer= (state = {}, action) =>{
    switch (action.type) {
        case BOOK_HISTORY_RETURN_REQUEST:
            return { loading: true }

        case BOOK_HISTORY_RETURN_SUCESS:
            return { loading: false, history_book_update: action.payload }

        case BOOK_HISTORY_RETURN_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}