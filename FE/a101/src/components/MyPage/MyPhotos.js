import * as React from "react";
import "./MyPhotos.css";

import { useSelector } from "react-redux";

export default function MyPhotos() {
  const userDetail = useSelector((state) => state.userDetail);

  return (
    <div>
      {userDetail.postDTOS.filter((item) => item.category === "photogroup") ===
        0 && <p>등록된 게시물이 없습니다</p>}

      <div className="container-gallery">
        {userDetail.postDTOS
          .filter((item) => item.category === "photogroup")
          .map((item) => (
            <div className="img-board"
            key={item.id}>
              <img
                className="image"
                src={item.url}
                alt={item.title}
                loading="lazy"
              />
              <div>{item.isShared ? '공유' : '비공개'}</div>
            </div>
          ))}
      </div>
    </div>
  );
}
