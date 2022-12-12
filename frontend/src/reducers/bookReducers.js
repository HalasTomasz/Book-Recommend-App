import {
    BOOK_LIST_REQUEST, 
    BOOK_LIST_SUCESS, 
    BOOK_LIST_FAIL,
    
    BOOK_DATA_REQUEST, 
    BOOK_DATA_SUCESS, 
    BOOK_DATA_FAIL,

} from '../constants/bookConstans'

export const bookListRedcurs= (state = {books: []}, action) =>{
    switch(action.type){
        case BOOK_LIST_REQUEST:

            return {loading: true, books: []}

        case BOOK_LIST_SUCESS:
            return {loading: false, books: action.payload}
        
        case BOOK_LIST_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}

export const bookDataRedcurs= (state = {book: {}}, action) =>{
    switch(action.type){
        case BOOK_DATA_REQUEST:
            return {loading: true, ...state}

        case BOOK_DATA_SUCESS:
            return {loading: false, book: action.payload}
        
        case BOOK_DATA_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}