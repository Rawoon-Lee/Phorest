import api from './api'

const s3 = {
  detailPost (postId) {
    return api({
      method: 'get',
      url: `download/${btoa(postId * 73 - 37)}/`,
    })
  },
  profileURL (data) {
    return api({
      method: 'post',
      url: `upload/profileimage/`,
      data: data,
      headers: {
        'Content-Type': 'multipart/form-data'
      },
    })
  }
}

export default s3