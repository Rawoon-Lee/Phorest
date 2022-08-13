import './FrameEdit.css'

import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'

import ImageEdit from '../components/Utils/ImageEdit'
import Layout from '../components/Layout/Layout'

import community from '../api/community'
import s3 from '../api/s3'
import mypage from '../api/mypage'
import { setDetailPost } from '../store/modules/community'

export default function FrameEdit() {
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const postId = (Number(atob(useParams().postId)) - 37) / 73

    const [type, setType] = useState(false)
    const [frameURL, setFrameURL] = useState('')
    const [content, setContent] = useState('')

    useEffect(() => {  // LTM2이면 new frame
        if (postId!==-1) {  // true 면 수정, false면 생성
            setType(true)
        }
    }, [])

    useEffect(() => {
        if (type) {
            community.detailPost(postId)
            .then(result => {
                if (result.data.category==="photogroup") {
                    navigate(`/community/${btoa((postId) * 73 + 37)}`)
                } else {
                    dispatch(setDetailPost(result.data))
                    setFrameURL(result.data.url)
                    setContent(result.data.content)
                }
            })
        }
    }, [postId, type])


    const editComplete = () => {
        let formdata = new FormData()
        formdata.append('content', content)
        formdata.append('image', null)

        community.editPost(postId, formdata)
        .then(result => {
            if (result.data===0) {
                navigate(`/community/${btoa(postId * 73 + 37)}`)
            } else {
                alert('잘못된 접근입니다')
            }
        })
    }


    return (
        <Layout>
            {
                type ?
                <div className='frame-edit-content'>
                    <p className='notice-frame'>✅ 권장되는 프레임의 사이즈는 가로: 1500px 세로: 1000px 입니다</p>
                    {
                        frameURL ? <img src={ frameURL } alt="frameImage"></img> : null
                    }

                    <label htmlFor="content">글 내용 : </label>
                    <input name="content" onChange={(e) => setContent(e.target.value)} type="text" id="content" defaultValue={content} />

                    <button onClick={editComplete}>완료</button>
                    <button onClick={() => navigate(-1)}>뒤로가기</button>
                </div> :
                <ImageEdit></ImageEdit>
            }
        </Layout>
    )
  }