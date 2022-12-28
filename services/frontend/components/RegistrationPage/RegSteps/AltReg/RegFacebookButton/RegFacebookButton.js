const RegFacebookButton = ({signIn}) => {
    return (
        <>
            <a onClick={signIn} className="alt-reg__btn alt-reg__btn--facebook">
                <svg viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="30" height="30" rx="15" fill="#1877F2"/>
                    <path d="M20.8389 19.3359L21.5039 15H17.3438V12.1875C17.3438 11.001 17.9238 9.84375 19.7871 9.84375H21.6797V6.15234C21.6797 6.15234 19.9629 5.85938 18.3223 5.85938C14.8945 5.85938 12.6562 7.93652 12.6562 11.6953V15H8.84766V19.3359H12.6562V29.8184C13.4209 29.9385 14.2031 30 15 30C15.7969 30 16.5791 29.9385 17.3438 29.8184V19.3359H20.8389Z" fill="white"/>
                </svg>

                Facebook
            </a>
        </>
    );
}

export default RegFacebookButton;