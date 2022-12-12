import {
    REVIEW_ADD_REQUEST, 
    REVIEW_ADD_SUCESS, 
    REVIEW_ADD_FAIL
} from '../constants/ReviewConstans'
import axios from 'axios'

export const addNewRating = (uid, book_id,review) => async (dispatch) => {
    try {
        
        dispatch({type: REVIEW_ADD_REQUEST})

        const { data } = await axios.post(
            '/api/review/add/',
            {'uid': uid , 'book_id': book_id, 'review':review}
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