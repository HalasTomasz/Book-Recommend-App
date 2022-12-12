import axios from 'axios'
import {
    REVIEW_ADD_REQUEST, 
    REVIEW_ADD_SUCESS, 
    REVIEW_ADD_FAIL,
} from './bookConstans'

export const registerReview = (review1,review2, books) => async (dispatch) => {
    try {
        
        dispatch({type: REVIEW_ADD_REQUEST})

        const { data } = await axios.post(
            '/api/users/review/',
            { 'review1': review1, 'review2':review2, 'books': books}
        )

        dispatch({
            type: REVIEW_ADD_SUCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: REVIEW_ADD_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}
