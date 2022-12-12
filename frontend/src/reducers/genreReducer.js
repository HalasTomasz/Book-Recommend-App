import axios from 'axios'
import {
    GENRE_LIST_REQUEST, 
    GENRE_LIST_SUCESS, 
    GENRE_LIST_FAIL,

    GENRE_USER_REQUEST,
    GENRE_USER_SUCESS,
    GENRE_USER_FAIL,

    GENRE_UPDATE_REQUEST, 
    GENRE_UPDATE_SUCESS, 
    GENRE_UPDATE_FAIL,
    
    GENRE_LIST_SHORT_REQUEST,
    GENRE_LIST_SHORT_SUCESS,
    GENRE_LIST_SHORT_FAIL,
} from '../constants/genreConstans'

export const getGenreListRedcurs= (state = {genres: []}, action) =>{

    switch(action.type){
        case GENRE_LIST_REQUEST:

            return {loading: true, genres: []}

        case GENRE_LIST_SUCESS:
            return {loading: false, genres: action.payload}
        
        case GENRE_LIST_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}

export const getGenreListShortRedcurs= (state = {genres_short: []}, action) =>{

    switch(action.type){
        case GENRE_LIST_SHORT_REQUEST:

            return {loading_genre: true, genres_short: []}

        case GENRE_LIST_SHORT_SUCESS:
            return {loading_genre: false, genres_short: action.payload}
        
        case GENRE_LIST_SHORT_FAIL:
            return {loading_genre: false, error_genre: action.payload}
        
        default:
            return state 
    }
}

export const getGenreUserRedcurs= (state = {user_genres: []}, action) =>{
    
    switch(action.type){
        case GENRE_USER_REQUEST:

            return {loading: true, user_genres: []}

        case GENRE_USER_SUCESS:
            return {loading: false, user_genres: action.payload}
        
        case GENRE_USER_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}

export const updateGenreUserRedcurs= (state = {}, action) =>{

    switch(action.type){
        case GENRE_UPDATE_REQUEST:
            return {loading: true}

        case GENRE_UPDATE_SUCESS:
            return {loading: false, new_user_genres: action.payload}
        
        case GENRE_UPDATE_FAIL:
            return {loading: false, error: action.payload}
        
        default:
            return state 
    }
}