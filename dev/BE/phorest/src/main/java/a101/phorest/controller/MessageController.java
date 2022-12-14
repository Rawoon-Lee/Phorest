package a101.phorest.controller;

import a101.phorest.domain.User;
import a101.phorest.dto.KakaoDTO;
import a101.phorest.dto.PostDTO;
import a101.phorest.dto.UserDTO;
import a101.phorest.jwt.TokenProvider;
import a101.phorest.repository.MyPageRepository;
import a101.phorest.service.*;
import lombok.RequiredArgsConstructor;
import net.nurigo.sdk.message.exception.NurigoMessageNotReceivedException;
import net.nurigo.sdk.message.model.Message;
import net.nurigo.sdk.message.response.MultipleDetailMessageSentResponse;
import net.nurigo.sdk.message.service.DefaultMessageService;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.net.MalformedURLException;
import java.util.*;


@RestController
@Component
@RequiredArgsConstructor
@RequestMapping("api")
public class MessageController {

    private final DefaultMessageService messageService;
    private final PostService postService;

    public final TokenProvider tokenProvider;

    public final UserService userService;
    private final KakaoService kakaoService;
    private final PhotoGroupService photoGroupService;
    private final MyPageService myPageService;
    private final MyPageRepository myPageRepository;

    @PostMapping("download/{postId}/message")
    public Long message(@PathVariable("postId") String postIdEncoded, @RequestHeader("Authorization") String token, @Valid @RequestBody Map<String, String> content){
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return 5L;
        Double decodedNumber = (Double.parseDouble(decodedString) + 37) / 73;
        Long postId = decodedNumber.longValue();

        String ct = content.get("content");
        String username = (String)tokenProvider.getTokenBody(token).get("sub");

        if(postId - decodedNumber != 0)
            return 5L; //???????????? ?????? post id
        if(!tokenProvider.validateToken(token))
            return 2L; //
        if(ct.length() > 100) return 6L; // ?????? ??????
        if(ct.trim().isEmpty()) return 7L; // ??????????????? ?????????
        return myPageService.setMessageMyself(postId,username,ct);
    }

//    @Scheduled(cron = "0 0 10 * * *")
    @PostMapping("sendkakao")
    public String sendMsg() throws Exception {
        List<PostDTO> postDTOS = postService.findMessagePosts();

        for(PostDTO postDTO : postDTOS){
            long postId = postDTO.getId() * 73 + 37;
            String encodedPostId = Base64.getEncoder().encodeToString(Long.toString(postId).getBytes());
            for(UserDTO userDTO : postDTO.getUsers()){
                if(userDTO.isKakao()){
                    String refresh_token = userDTO.getRefresh_token();
                    String accessToken = kakaoService.getAccessToken(refresh_token);
//                    String accessToken = userDTO.getAccess_token();
                    String path = photoGroupService.findOne(postDTO.getPhotogroupId()).getPhotoGroupPath();
                    String content = myPageService.getMessageByPostIdAndUsername(postDTO.getId(), userDTO.getUsername());
                    KakaoDTO kakaoDTO = new KakaoDTO();
                    kakaoDTO.setPath(path);
                    kakaoDTO.setAccessToken(accessToken);
                    kakaoDTO.setEncodedPostId(encodedPostId);
                    kakaoService.sendMessage(kakaoDTO,content);

//                    kakaoDTOList.add(kakaoDTO);
                }
            }

        }
        return "success";
    }

    //@Scheduled(cron = "0 0 9 * * ?")
    public void sendMessages() throws MalformedURLException, IOException {
        List<Message> messageList = new ArrayList<>();
        List<PostDTO> postDTOS = postService.findMessagePosts();
        for(PostDTO postDTO : postDTOS){
            long postId = postDTO.getId() * 73 + 37;
            String encodedPostId = Base64.getEncoder().encodeToString(Long.toString(postId).getBytes());
            for(UserDTO userDTO : postDTO.getUsers()){
                if(userDTO.getPhone() == null)
                    continue;
//                File f = new File(System.getProperty("user.dir") + "/imagefiles/tempfiles/" + userDTO.getPhone());
//                FileUtils.copyURLToFile(new URL(postDTO.getUrl()), f);
//                String imageId = this.messageService.uploadFile(f, StorageType.MMS, null);
//                f.delete();
                Message message = new Message();
                // ???????????? ??? ??????????????? ????????? 01012345678 ????????? ??????????????? ?????????.
                message.setFrom("01040563512");
                message.setTo(userDTO.getPhone());
                message.setText("????????? ??? ????????? ????????? ????????? ?????????\n" + "phorest.site/community/" + encodedPostId);
//                message.setImageId(imageId);
                messageList.add(message);
            }
        }
        try {
            // send ???????????? ?????? Message ????????? ????????? ???????????????!
            MultipleDetailMessageSentResponse response = this.messageService.send(messageList);

            // ?????? ??????????????? ???????????? ????????? ?????? ??? ?????? ?????? ??????????????? ????????? ??????????????????!
            //MultipleDetailMessageSentResponse response = this.messageService.send(messageList, true);
            System.out.println(response);
        } catch (NurigoMessageNotReceivedException exception) {
            System.out.println(exception.getFailedMessageList());
            System.out.println(exception.getMessage());
        } catch (Exception exception) {
            System.out.println(exception.getMessage());
        }
    }
    @PostMapping("api/user/sendsms")
    @ResponseBody
    public String sendSMS(@RequestBody HashMap<String, String> input) {
        if(input.get("phone") == null)
            return "1";
        Random rand  = new Random();
        String numStr = "";
        for(int i=0; i<4; i++) {
            String ran = Integer.toString(rand.nextInt(10));
            numStr+=ran;
        }
        Message message = new Message();
        message.setFrom("01040563512");
        message.setTo(input.get("phone"));
        message.setText("Phorest ????????? ?????? ????????? : ??????????????? " + "[" + numStr + "]" + "?????????");
        try {
            // send ???????????? ?????? Message ????????? ????????? ???????????????!
            MultipleDetailMessageSentResponse response = this.messageService.send(message);

            // ?????? ??????????????? ???????????? ????????? ?????? ??? ?????? ?????? ??????????????? ????????? ??????????????????!
            //MultipleDetailMessageSentResponse response = this.messageService.send(messageList, true);
            System.out.println(response);
        } catch (NurigoMessageNotReceivedException exception) {
            System.out.println(exception.getFailedMessageList());
            System.out.println(exception.getMessage());
        } catch (Exception exception) {
            System.out.println(exception.getMessage());
        }
        return numStr;
    }
}
