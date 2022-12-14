import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'

import './Download.css'
import Layout from './../components/Layout/Layout'
import CommunityCarousel from './../components/Community/CommunityCarousel'
import MsgEdit from './../components/Utils/MsgEdit'

// functions
import { setDetailPost } from '../store/modules/community'
import s3 from './../api/s3'
import mypage from './../api/mypage'
import { setPostForKakao } from '../store/modules/mypage'


export default function Main() {
    const navigate = useNavigate()
    const dispatch = useDispatch()
    
    const postId = (Number(atob(useParams().postId)) + 37) / 73

    let content = useSelector(state => state.detailPost)
    const currentUser = useSelector(state => state.currentUser)
    const [isOwned, setIsOwned] = useState(false)
    const [isEditing, setIsEditing] = useState(false)


    useEffect(() => {
        s3.detailPost(postId)
        .then(result => {
            dispatch(setDetailPost(result.data))
        })
    }, [currentUser])

    useEffect(() => {
        if (content.category==='frame') {navigate(-1)}
        if (content) {dispatch(setPostForKakao(content.id))}
    }, [content])

    useEffect(() => {
        if (!currentUser.username || !currentUser.kakao || !isOwned) {
            setIsEditing(false)
        }
        if (!isOwned && currentUser.username) {
            mypage.ownPost(postId)
            .then(result => {
                if (result.data) {
                    setIsOwned(true)
                } else {
                    setIsOwned(false)
                }
            })
        }
    }, [currentUser])

    const imageDownload = () => {
        fetch(content.url + '?timestamp=2')
        .then((image) => {
            return image.blob()
        })
        .then((blob) => {
            const url = window.URL.createObjectURL(blob)
            const a = document.createElement("a")
            a.href = url
            a.download = `PhoRest_${content.time.slice(0, 10)}.png`
            a.click()
            a.remove()
            window.URL.revokeObjectURL(url)
        })
    }

    const videoDownload = () => {
        fetch(content.videoURL + '?timestamp=2')
        .then((image) => {
            return image.blob()
        })
        .then((blob) => {
            const url = window.URL.createObjectURL(blob)
            const a = document.createElement("a")
            a.href = url
            a.download = `PhoRest_${content.time.slice(0, 10)}.mp4`
            a.click()
            a.remove()
            window.URL.revokeObjectURL(url)
        })
    }

    return (
        <Layout>
            <main>
                {
                    !currentUser.username ?
                    <h5 className='notice'>???? ????????? ????????? ?????????????????? ????????? ????????? ??? ???????????? ???</h5> :
                    null
                }
                <div className="download-img" onClick={() => navigate(`/community/${btoa((postId) * 73 + 37)}`)}>
                    <img src={content.url} alt={content.content} />
                </div>
                <br />
                <div className='download-utils'>
                    <div className="download-links">
                        <div className="download-links-item download-picture" onClick={() => imageDownload()}>
                            <p>????</p>
                            <p>?????? ????????????</p>
                        </div>
                        <div className="download-links-item download-video" onClick={() => videoDownload()}>
                            <p>????</p>
                            <p>????????? ????????????</p>
                        </div>
                    </div>
                    <div className='download-msg'>
                        {
                            currentUser.username && isOwned ?
                            <div className="download-links-item" onClick={() => setIsEditing(!isEditing)}>
                                <p>????</p><p className='download-links-long'>?????? ????????? ????????? ??????</p>
                            </div> :
                            null
                        }
                        {
                            isEditing ?
                            <MsgEdit setIsEditing={setIsEditing} postId={postId}></MsgEdit> :
                            null
                        }
                    </div>
                </div>
                <br />

                <div className="download-community">
                    <div>
                        <CommunityCarousel communityType="photogroup" />
                    </div>
                    <div>
                        <CommunityCarousel communityType="frame" />
                    </div>
                </div>
            </main>
        </Layout>
    )
}