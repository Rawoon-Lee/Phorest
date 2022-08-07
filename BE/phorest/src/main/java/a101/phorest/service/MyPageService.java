package a101.phorest.service;

import a101.phorest.domain.*;
//import a101.phorest.repository.MemberRepository;
import a101.phorest.dto.PostDTO;
import a101.phorest.dto.UserDTO;
import a101.phorest.repository.FollowRepository;
import a101.phorest.repository.MyPageRepository;
import a101.phorest.repository.PostRepository;
import a101.phorest.repository.UserRepository;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@Getter @Setter
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class MyPageService {
    private final UserRepository userRepository;
    private final PostRepository postRepository;
    private final MyPageRepository myPageRepository;

    private final FollowRepository followRepository;
    @Transactional
    public Long join(Long postId, String username)
    {
        Optional<MyPage> myPage = myPageRepository.findByPostIdAndUsername(postId, username);
        if(myPage.isPresent())
            return 1L;
        MyPage mypage = new MyPage();
        User user = userRepository.findByUsername(username);
        Post post = postRepository.findById(postId).get();
        mypage.setUser(user);
        mypage.setPost(post);
        mypage.setShared(false);
        mypage.setCategory(post.getCategory());
        myPageRepository.save(mypage);
        return mypage.getId();
    }

    public UserDTO findByUserId(String searchUsername, String loginUsername)
    {
        User searchUser = userRepository.findByUsername(searchUsername);
        User loginUser = new User();
        if(!loginUsername.equals(""))
            loginUser = userRepository.findByUsername(loginUsername);
        if(searchUser == null)
            return new UserDTO();
        UserDTO userDto = UserDTO.from(searchUser);
        List<Post> posts;
        if(searchUsername.equals(loginUsername))
        {
            posts = postRepository.findByUserId(searchUsername);
            userDto.setFollowingCount(followRepository.countFollowByFollower(searchUser));
        }
        else
        {
            posts = postRepository.findByUserIdShared(searchUsername);
            Optional<Follow> follow = Optional.empty();
            if(!loginUsername.equals(""))
                follow = followRepository.findByFollowerAndFollowing(searchUser.getUserId(), loginUser.getUserId());
            if(follow.isPresent())
                userDto.setFollowing(true);
            else
                userDto.setFollowing(false);
        }
        userDto.setFollowerCount(followRepository.countFollowByFollowing(searchUser));
        List<PostDTO> postDTOS = new ArrayList<>();
        for(int i = 0; i < posts.size(); i++)
        {
            PostDTO postDto = new PostDTO(posts.get(i), new ArrayList<>());
            postDTOS.add(postDto);
        }
        userDto.setPostDTOS(postDTOS);
        return userDto;
    }

    public List<UserDTO> findByPostId(Long postId)
    {
        List<User> users = userRepository.findByPostId(postId);
        List<UserDTO> userDTOS = new ArrayList<>();
        for(int i = 0; i < users.size(); i++) {
            UserDTO userDto = UserDTO.from(users.get(i));
            userDTOS.add(userDto);
        }
        return userDTOS;
    }

    public Long sharePost(Long postId, String username){
        Optional<Post> post = postRepository.findById(postId);
        if(post.isEmpty())
            return 2L;
        Optional<MyPage> myPage = myPageRepository.findByPostIdAndUsername(postId, username);
        if(myPage.isEmpty())
            return 3L;
        myPage.get().setShared(true);
        if(!post.get().isShared())
            post.get().setShared(true);
        return 0L;
    }
}
