import { _get, _post, _delete, _put } from './helper'

// default - MODEL_RESTFUL
const MODEL_TRADITION = 0
const MODEL_RESTFUL = 1
const MODEL_NO = 2

// login
const _login = _post('/user/signin/')
// logout
const _logout = _post('/user/signout/')
// register
const _register = _post('/user/register/')
// user
const _getUserInfo = _get('/user/get_user_info/')
const _deleteUser = _delete('/user/deleteUserByID/')
const _changePassword = _post('/user/changePasswordByID/')
const _editUser = _put('/user/updateUserByID/')
// game
const _getGame = _get('/game/getGameByGameID/')
const _getRecommendGame = _get('/game/getRecommendGameByUserID/')
// banner
const _getBannerList = _get('/banner/getBannerList/')
const _getBannerDetail = _get('/banner/getBannerDetailByBannerID/')
// comment
const _addComment = _post('/comment/addCommentByUserID/')
const _getGameCommentByGameID = _get('/comment/getGameCommentByGameID/')
const _deleteComment = _delete('/comment/deleteCommentByCommentID/')
// category
const _getCategory = _get('/gameType/list/')
const _getCategoryList = _get('/gameType/page/')
const _addCategory = _post('/gameType/insert/')
const _editCategory = _put('/gameType/updateIgnoreNull/')
const _deleteCategory = _delete('/gameType/delete/')
// log
const _getLogList = _get('/logs/page/')
const _deleteLog = _delete('/logs/delete/')
// upload
const _uploadFile = _post('/uploadfile/')
// star
const _getStar = _get('/likeGame/list/')
const _addStar = _post('/likeGame/insert/')
const _deleteStar = _delete('/likeGame/delete/')
export {
    // login
    _login,
    // logout
    _logout,
    // register
    _register,
    // user
    _getUserInfo,
    _deleteUser,
    _changePassword,
    _editUser,
    // game
    _getGame,
    _getRecommendGame,
    // banner
    _getBannerList,
    _getBannerDetail,
    // category
    _getCategory,
    _getCategoryList,
    _addCategory,
    _editCategory,
    _deleteCategory,
    // comment
    _addComment,
    _getGameCommentByGameID,
    _deleteComment,
    // log
    _getLogList,
    _deleteLog,
    // upload
    _uploadFile,
    // star
    _getStar,
    _addStar,
    _deleteStar
}
