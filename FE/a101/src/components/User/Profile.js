import { useNavigate } from 'react-router-dom'
import { useSelector } from 'react-redux'

import AccountCircleTwoToneIcon from "@mui/icons-material/AccountCircleTwoTone";
import './Profile.css'

export default function Profile(props) {
    const navigate = useNavigate()

    let user = useSelector(state => state.currentUser)
    if (props.user) {
        user = props.user
    }


    return (
        <div className="profile" onClick={() => {navigate(`/mypage/${user.username}`)}}>
           {
            user.profileURL ? <img src={user.profileURL} alt="" /> : <AccountCircleTwoToneIcon className="header-profile" />
           }
           {user.nickname}
        </div>
    )
  }