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


export const userUpdateReducer = (state = {}, action) => {

    switch (action.type) {
        case USER_UPDATE_REQUEST:
            return { loading: true }

        case USER_UPDATE_SUCESS:
            return { loading: false, user_update: action.payload }

        case USER_UPDATE_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}

export const userRegisterReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_ADD_REQUEST:
            return { loading: true }

        case USER_ADD_SUCESS:
            return { loading: false, user_new: action.payload }

        case USER_ADD_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}

export const userGetterReducer = (state = {user: {}}, action) => {

    switch (action.type) {
        case USER_GET_REQUEST:
            return { loading: true,  ...state }

        case USER_GET_SUCESS:
            return { loading: false, user: action.payload }

        case USER_GET_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}

export const userGetterRecomenderReducer = (state = {recomendation: {}}, action) => {

    switch (action.type) {
        case USER_RECOMENDATIONS_REQUEST:
            return { loading: true,  ...state }

        case USER_RECOMENDATIONS_SUCESS:
            return { loading: false, recomendation: action.payload }

        case USER_RECOMENDATIONS_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}