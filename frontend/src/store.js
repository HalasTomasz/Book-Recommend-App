import {createStore, combineReducers, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import {bookListRedcurs, bookDataRedcurs} from './reducers/bookReducers'
import {getListHistoryReducer, setListHistoryReducer, updateListHistoryReducer} from './reducers/historyReducer'
import {userRegisterReducer,userGetterReducer,userUpdateReducer, userGetterRecomenderReducer } from './reducers/userReducer'
import { getGenreListRedcurs, getGenreUserRedcurs, updateGenreUserRedcurs, getGenreListShortRedcurs } from './reducers/genreReducer'

const reducer = combineReducers({

    bookList: bookListRedcurs,
    bookData: bookDataRedcurs,
    
    getUserDataAlgo:userGetterRecomenderReducer,
    getShortGenre:getGenreListShortRedcurs,
    
    getUserHistory: getListHistoryReducer,
    setUserHistory: setListHistoryReducer,
    returnBookUserHistory:updateListHistoryReducer,
    getUserGenre:getGenreUserRedcurs,
    getGenre:getGenreListRedcurs,
    updateUserGenre:updateGenreUserRedcurs,

    userRegister: userRegisterReducer,
    getUser: userGetterReducer,
    updateUser:userUpdateReducer,
})



const middleware = [thunk]

const store = createStore( reducer,
    composeWithDevTools(applyMiddleware(...middleware
    )) )

export default store
