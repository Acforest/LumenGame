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
const _getUserInfo = _get('/user/user_info/')
const _changePassword = _post('/user/user_info/')
const _editUserInfo = _put('/user/user_info/')
// game
const _getGame = _get('/game/get_game/')
const _getRank = _get('/game/get_rank/')
const _getRecGame = _get('/game/get_rec_game/')
const _searchGame = _get('/game/get_search_game/')
const _searchTag = _get('/game/get_search_tag/')
const _likeGame = _post('/game/like_game/')
const _cancelLikeGame = _post('/game/cancel_like_game/')
const _getGameDetail = _get('/game/get_game_detail/')
// repository
const _getRepositoryGame = _get('/repository/get_repository_game/')
const _searchRepositoryGame = _get('/repository/search_repository_game/')
const _searchRepositoryTag = _get('/repository/search_repository_tag/')
// banner
const _getBannerList = _get('/banner/get_banner/')
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
    _changePassword,
    _editUserInfo,
    // game
    _getGame,
    _getRank,
    _getRecGame,
    _searchGame,
    _searchTag,
    _likeGame,
    _cancelLikeGame,
    _getGameDetail,
    // repository
    _getRepositoryGame,
    _searchRepositoryGame,
    _searchRepositoryTag,
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
