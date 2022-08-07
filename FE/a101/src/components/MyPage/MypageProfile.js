import "./MypageProfile.css";
import defaultProfile from "../../assets/defaultProfile.png";

import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch ,useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { setIsFollowing } from "../../store/modules/mypage"

import Modal from "react-bootstrap/Modal";

// 공유 활성/비활성 설정하기
import user from "../../api/user";

export default function MypageProfile(props) {
  // 프로필 이미지 없을 때 대체 이미지 나오게 하는 함수
  const handleImgError = (e) => {
    e.target.src = defaultProfile;
  };
  // 데이터 가져오기
  const userDetail = useSelector((state) => state.userDetail);

  // 해당 게시물이 현재 로그인한 유저의 게시물인지 확인
  const { username } = useParams();
  const currentUser = useSelector((state) => state.currentUser);
  let isOwner = username === currentUser.username ? true : false;
  // console.log(currentUser)

  // 로그인 안되어있는채로 팔로우버튼을 누르면 로그인창으로 안내하는 모달창 나옴
  const [show, setShow] = useState(false);
  // 모달
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  // 이동
  const navigate = useNavigate();
  // 숫자 세기
  let picCnt = userDetail.postDTOS.filter(
    (item) => item.category === "photogroup"
  ).length;
  let frameCnt = userDetail.postDTOS.filter(
    (item) => item.category === "frame"
  ).length;

  // 팔로우 버튼 누르면 신청
  const dispatch = useDispatch();
  function follow() {
    user.follow(username).then((result) => {
      console.log(result.data)
      dispatch(setIsFollowing(result.data))
    })
  }
  // const [profile, setProfile] = useState([]);
  // useEffect(() => {
  //   setProfile(userDetail);
  // }, [userDetail]);

  return (
    <div>
      <div className="profile-box">
        <img
          className="profile-img"
          src={props.profileUrl}
          alt="프로필"
          onError={handleImgError}
        />
        <div className="info">
          <div className="num">{picCnt}</div>
          <div className="name">게시글</div>
        </div>
        <div className="info">
          <div className="num">{frameCnt}</div>
          <div className="name">프레임</div>
        </div>
        <div className="info">
          <div className="num">{userDetail.followerCount}</div>
          <div className="name">팔로워</div>
        </div>
      </div>
      <div className="memo">{userDetail.introduce}</div>
      {isOwner && <button>프로필 수정하기</button>}
      <div className="modal-button">
        {currentUser.username ? (
          userDetail.following ? 
          <button className="button-unfollow" onClick={follow}>팔로우 취소하기</button> :
          <button className="button-follow" onClick={follow}>팔로우 하기</button>
        ) : (
          <button variant="primary" onClick={handleShow}>
            팔로우하기
          </button>
        )}

        <Modal
          show={show}
          onHide={handleClose}
          backdrop="static"
          keyboard={true}
          centered
          className="modal"
        >
          <Modal.Body>
            로그인이 필요한 기능입니다.
            <br></br>
            로그인 하시겠습니까?
          </Modal.Body>
          <Modal.Footer>
            <button variant="secondary" onClick={handleClose}>
              다음에 할게요
            </button>
            <button variant="primary" onClick={() => navigate("/login")}>
              로그인 할래요
            </button>
          </Modal.Footer>
        </Modal>
      </div>
    </div>
  );
}
