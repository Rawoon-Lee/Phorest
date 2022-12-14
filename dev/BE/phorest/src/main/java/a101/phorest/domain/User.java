package a101.phorest.domain;

import lombok.*;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "user")
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class User {

   @Id
   @Column(name = "user_id")
   @GeneratedValue(strategy = GenerationType.IDENTITY)
   private Long userId;

   @Column(name = "username", length = 50, unique = true)
   private String username;

   @Column(name = "password", length = 100)
   private String password;

   @Column(name = "nickname", length = 50)
   private String nickname;

   @Column(name = "activated")
   private boolean activated;

   @Enumerated(EnumType.STRING)
   @Column(name = "role")
   private Role role;

   //@Length(min = 10, max = 16)
   @Column(name = "phone", unique = true)
   private String phone;

   private String profileURL;

   @Column(name = "iskakao")
   private boolean isKakao;

   private String introduce;

   private String refresh_token;
   private String access_token;

   @OneToMany(mappedBy = "user")// Post - comments 하나의 멤버가 여러개의 댓글을 달을 수 있다. 일대다. mypage가 주인장.
   private List<MyPage> mypages = new ArrayList<>();

   @OneToMany(mappedBy = "user")//Post - comments 하나의 멤버가 여러개의 댓글을 달을 수 있다. 일대다. comment가 주인장.
   private List<Comment> comments = new ArrayList<>();

   @OneToMany(mappedBy = "user")//Post - comments 하나의 멤버가 여러개의 댓글을 달을 수 있다. 일대다. like가 주인장.
   private List<Like> likes = new ArrayList<>();

   @OneToMany(mappedBy = "user")//Post - comments 하나의 멤버가 여러개의 댓글을 달을 수 있다. 일대다. bookmark가 주인장.
   private List<Bookmark> bookmarks = new ArrayList<>();

   @OneToMany(mappedBy = "following")
   private List<Follow> followings = new ArrayList<>();

   @OneToMany(mappedBy = "follower")
   private List<Follow> followers = new ArrayList<>();

}
