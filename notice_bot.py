import discord
client = discord.Client()
@client.event
async def on_ready():
    print('\n준비 완료\n작동 중지를 원하신다면 컨트롤 + C를 눌러주세요')
    print('\n명령어 목록')
    print('\n!공지 추가 공지 ["색코드" "제목"]\n예: !공지 추가 공지 "ffffff" "공지입니다."\n새로운 공지를 만듭니다.\n이미 만들어져있는 공지가 있다면 덮어쓰기합니다.')
    print('\n!공지 추가 필드 ["필드제목" "내용"]\n예: !공지 추가 필드 "필드1" "필드입니다."\n새로운 필드를 추가합니다.')
    print('\n!공지 삭제 필드 [번호]\n예: !공지 삭제 필드 1\n[번호]번째 필드를 삭제합니다. 번호는 0부터 시작합니다.')
    print('\n!공지 보내기 [채팅채널]\n예: !공지 보내기 #일반채팅\n[채팅채널]에 공지를 보냅니다.')
    print('\n!공지 필드목록\n필드목록을 보여줍니다.')
    
@client.event
async def on_message(message):

    global embed
    
    if message.author.bot:
        return None
    
    if message.content.startswith('!공지 추가 공지'):

        msg = message.content
        msg = msg.split('"')
        color = msg[1]
        main = msg[3]
        color = "0x"+color
        color = int(color,16)

        embed = discord.Embed(title=main, color=color)

        await message.channel.send(embed=embed)
    
    if message.content.startswith('!공지 추가 필드'):
    
        msg = message.content
        msg = msg.split('"')
        title = msg[1]
        value = msg[3]
        embed.add_field(name=title, value=value, inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('!공지 삭제 필드'):
    
        msg = message.content
        msg = msg.split()
        title = msg[3]
        embed.remove_field(int(title))

        await message.channel.send(embed=embed)

    if message.content.startswith('!공지 보내기'):
        msg = message.content
        msg = msg.split()
        ch = msg[2]
        ch = ch[2:-1]

        ch = client.get_channel(int(ch))

        await ch.send(embed=embed)

    if message.content.startswith('!공지 필드목록'):

        fds = embed.fields
        fds = str(fds)
        fds = fds.split(',')
        sq = -1
        embed_list = discord.Embed(title='필드목록', color=0x00ff56)
        for i in range(1,len(fds)):
            
            if fds[i].find('name') == -1:
                if fds[i].find('value') == -1:
                    None

                else:
                    if i == len(fds)-1:
                        sq += 1
                        fds[i] = fds[i][8:-3]
                        fds[i] = '제목: '+fds[i-1]+'\n내용: '+fds[i]
                        embed_list.add_field(name=str(sq), value=fds[i], inline=False)

                    else:
                        sq += 1
                        fds[i] = fds[i][8:-2]
                        fds[i] = '제목: '+fds[i-1]+'\n내용: '+fds[i]
                        embed_list.add_field(name=str(sq), value=fds[i], inline=False)

            else:
                fds[i] = fds[i][7:-1]
                fds[i] = fds[i]

        await message.channel.send(embed=embed_list)

client.run('TOKEN')
