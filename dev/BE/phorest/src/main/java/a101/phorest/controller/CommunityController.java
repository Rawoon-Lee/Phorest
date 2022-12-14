package a101.phorest.controller;
import a101.phorest.S3Uploader;
import a101.phorest.domain.Post;
import a101.phorest.dto.OffsetDTO;
import a101.phorest.dto.PostDTO;
import a101.phorest.jwt.TokenProvider;
import a101.phorest.repository.PostRepository;
import a101.phorest.service.FrameService;
import a101.phorest.service.PostService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.Optional;

@RestController
@RequiredArgsConstructor
@RequestMapping("api/community")
public class CommunityController {

    private final PostService postService;

    private final TokenProvider tokenProvider;
    private final S3Uploader s3Uploader;
    private final FrameService frameService;

    private final PostRepository postRepository;
    @PostMapping("photogroup/like")
    @ResponseBody
    public List<PostDTO> photoGroupLikeDownload(@RequestBody OffsetDTO offsetDto,@RequestHeader(value = "Authorization", required = false) String token)
    {
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            return postService.findByLikeCount("photogroup" ,offsetDto.getLimit(), offsetDto.getOffset(), offsetDto.getHumanCount(),"");
        }
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.findByLikeCount("photogroup" ,offsetDto.getLimit(), offsetDto.getOffset(), offsetDto.getHumanCount(),username);
    }

    @PostMapping("photogroup/recent")
    @ResponseBody
    public List<PostDTO> photoGroupRecentDownload(@RequestBody OffsetDTO offsetDto, @RequestHeader(value = "Authorization", required = false) String token)
    {
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            return postService.findByRecent("photogroup" ,offsetDto.getLimit(), offsetDto.getOffset(), offsetDto.getHumanCount(),"");
        }
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.findByRecent("photogroup" ,offsetDto.getLimit(), offsetDto.getOffset(), offsetDto.getHumanCount(),username);
    }

    @GetMapping("frame/{frameId}")
    @ResponseBody
    public Long findFramePostId(@PathVariable("frameId") Long frameId){
        return postService.findPostByFrameId(frameId);
    }

    @PostMapping("frame/like")
    @ResponseBody
    public List<PostDTO> frameLikeDownload(@RequestBody OffsetDTO offsetDto, @RequestHeader(value = "Authorization", required = false) String token)
    {
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            return postService.findByLikeCount("frame" ,offsetDto.getLimit(), offsetDto.getOffset(), 0L,"");
        }
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.findByLikeCount("frame" ,offsetDto.getLimit(), offsetDto.getOffset(), 0L,username);
    }

    @PostMapping("frame/recent")
    @ResponseBody
    public List<PostDTO> FrameRecentDownload(@RequestBody OffsetDTO offsetDto, @RequestHeader(value = "Authorization", required = false) String token)
    {
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            return postService.findByRecent("frame" ,offsetDto.getLimit(), offsetDto.getOffset(), 0L,"");
        }
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.findByRecent("frame" ,offsetDto.getLimit(), offsetDto.getOffset(), 0L,username);
    }

    @GetMapping("frame/count")
    @ResponseBody
    public Long frameCount()
    {
        List<Post> posts = postRepository.countFramePostsByCategory("frame");
        return (long)posts.size();
    }

    @GetMapping("photogroup/count")
    @ResponseBody
    public Long photogroupCount(@RequestParam("humanCount") Long humanCount )
    {
        List<Post> posts = postRepository.countPhotogroupPostsByCategory("photogroup", humanCount);
        return (long)posts.size();
    }

    @GetMapping("{postId}")
    public PostDTO getPost(@PathVariable("postId") String postIdEncoded, @RequestHeader(value = "Authorization", required = false) String token)
    {
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return new PostDTO();
        Double decodedNumber = (Double.parseDouble(decodedString) - 37) / 73;
        Long postId = decodedNumber.longValue();
        if(postId - decodedNumber != 0)
            return new PostDTO();
        Optional<PostDTO> postDto;
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            postDto = postService.findDtoOne(1L, postId, "");
            return postDto.orElseGet(PostDTO::new);
        }
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        postDto = postService.findDtoOne(1L, postId, username);
        return postDto.orElseGet(PostDTO::new);
    }

    @PutMapping("{postId}")
    public Long editPost(@PathVariable("postId") String postIdEncoded, @RequestPart(value = "image", required = false) MultipartFile multipartFile,@RequestParam("content") String content, @RequestHeader(value = "Authorization") String token){
        String uploadUrl = null;
        Long frameId = null;
        if(multipartFile != null)
        {
            try {
                uploadUrl = s3Uploader.uploadFiles(multipartFile, "frame");
                frameId = frameService.join(uploadUrl);
            } catch (Exception e) {
                return -1L;
            }
        }
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return 4L;
        Double decodedNumber = (Double.parseDouble(decodedString) - 37) / 73;
        Long postId = decodedNumber.longValue();
        if(postId - decodedNumber != 0)
            return 4L;
        if(!tokenProvider.validateToken(token))
            return 1L;
        if(content.length() > 255) return 6L;
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.editPost(postId, username,content,frameId);
    }

    @DeleteMapping("{postId}")
    public Long deletePost(@PathVariable("postId") String postIdEncoded, @RequestHeader(value = "Authorization") String token){
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return 4L;
        Double decodedNumber = (Double.parseDouble(decodedString) - 37) / 73;
        Long postId = decodedNumber.longValue();
        if(postId - decodedNumber != 0)
            return 4L;
        if(!tokenProvider.validateToken(token))
            return 1L;
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return postService.deletePost(postId, username);
    }
}
